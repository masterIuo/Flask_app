# 生成两段随机文本
from flask import *
from jinja2.utils import generate_lorem_ipsum

app = Flask(__name__)


@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)  # 生成两段随机文本
    return '''
    <h1>A very long post</h1>
    <div class="body">%s</div>
    <button id="load">load more</button>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script type="text/javascript">
    $(function(){
        $('#load').click(function(){
            $.ajax({
                url:'/more',
                type:'get',
                success:function(data){
                    $('.body').append(data);
                }
            })
        })
    })
    </script>''' % post_body


@app.route('/more')
def moretext():
    return generate_lorem_ipsum(n=1)


if __name__ == '__main__':
    app.run()
