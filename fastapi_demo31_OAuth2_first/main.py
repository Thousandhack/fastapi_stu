"""


OAuth2用户
OAuth2是一个规范，定义了几种处理身份验证和授权的方式。

它是一个相当广泛的规范，涵盖了几个复杂的用例。

它包括使用“第三方”进行身份验证的方法。


OAuth 1
有一个OAuth 1，它与OAuth2完全不同，并且更为复杂，因为它直接包含有关如何加密通信的规范。

它现在不是很流行或使用。

OpenID Connect
OpenID Connect是另一个基于 OAuth2的 规范 。

它只是扩展了OAuth2，以指定一些在OAuth2中相对模糊的内容，以尝试使其更具互操作性。

例如，Google登录使用OpenID Connect（在下面使用OAuth2）。

但是，Facebook登录不支持OpenID Connect。 它具有自己的OAuth2风格。

OpenID（不是“ OpenID Connect”）
还有一个“ OpenID”规范。 那试图解决与 OpenID Connect 相同的问题 ，但不是基于OAuth2。

因此，它是一个完整的附加系统。

它现在不是很流行或使用。

OpenAPI的
OpenAPI（以前称为Swagger）是用于构建API（现已成为Linux Foundation的一部分）的开放规范。

FastAPI 基于 OpenAPI 。

这就是使多个自动交互式文档界面，代码生成等成为可能的原因。

OpenAPI具有定义多个安全“方案”的方法。

通过使用它们，您可以利用所有这些基于标准的工具，包括这些交互式文档系统。

OpenAPI定义了以下安全方案：

apiKey ：特定于应用程序的密钥，可以来自：
查询参数。
标头。
一块饼干。
http ：标准的HTTP身份验证系统，包括：
bearer ：标题 Authorization 的值 Bearer 加上令牌。 这是从OAuth2继承的。
HTTP基本身份验证。
HTTP摘要等
oauth2 ：所有OAuth2处理安全性的方式（称为“流程”）。
其中一些流程适合构建OAuth 2.0身份验证提供程序（例如Google，Facebook，Twitter，GitHub等）：
implicit
clientCredentials
authorizationCode
但是，有一个特定的“流”可以完美地用于直接在同一应用程序中处理身份验证：
password ：接下来的几章将介绍此示例。
openIdConnect ：具有定义自动发现OAuth2身份验证数据的方式。
此自动发现是OpenID Connect规范中定义的内容。
小费

集成其他身份验证/授权提供者（例如Google，Facebook，Twitter，GitHub等）也是可能的，而且相对容易。

最复杂的问题是建立像这样的身份验证/授权提供程序，但是 FastAPI 为您提供了轻松完成任务的工具，同时又为您带来了繁重的工作。
"""

"""
FastAPI 实用程序
FastAPI为 fastapi.security 模块中的 每个安全方案提供了几种工具，这些工具 简化了这些安全机制的使用。

在下一章中，您将看到如何使用 FastAPI 提供的那些工具为API添加安全性 。
"""
