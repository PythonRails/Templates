from pythonrails_templates import BaseTemplate


class Template(BaseTemplate):
    """
    Compiled template from 'templates/base.html'.
    """

    def __init__(self):
        self.use('bootstrap3.0')

        self.tag_head(
            self.tag_title(
                self.var_title,
                'Test template rendering'
            )
        )

        self.tag_body(
            self.tag_div(
                self.tag_div(
                    self.tag_a('Home page', href='/'),
                    self.tag_a('Blog', href='/blog'),
                    self.var_sidebar_links,
                    _class='col-md-4'
                ),

                self.tag_div(
                    self.tag_div(
                        self.var_top_menu_content,
                        _class='top_menu'
                    ),
                    self.var_page_content,
                    _class='col-md-8'
                ),

                _class='row'
            ),

            self.tag_div(
                self.tag_div(
                    self.tag_a('Home page', href='/'),
                    self.tag_a('Blog', href='/blog'),
                    self.var_bottom_menu_links,
                    _class='bottom_menu col-md-12'
                ),

                _class='row'
            )
        )
