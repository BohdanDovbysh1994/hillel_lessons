# https://admin-demo.nopcommerce.com/
# XPATH
# by tag $x('//h1')
# by tag $x('//label')
# by tag attribute for $x('//label[@for="Password"]')
# By id "//*[@id='Password']"

# With | and statement $x("//div[@class='inputs']/label[@for='Email'] | //div[@class='inputs']/label[@for='Password']")
# $x("//div[@class='inputs']//ancestor::label")
# Parent:
# Child: $x("//div[@class='inputs']/child::*")
# $x("//input[@class='email valid']/preceding::label")
# $x("//input[@class='email valid']/preceding-sibling::label")
# $x("//input[@class='email valid']/following-sibling::*")
# $x("//label[text()='Email:']/parent::div")


# CSS
# $$('label[for="Password"]')
# $$("div label[for]")
# $$(".field-validation-valid")
# By id $$("#Password")
# By attribute $$('[for]')
# direct child "tag > tag"
# child or sub child "tag tag"
# combine $$("div > form strong")
