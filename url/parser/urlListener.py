# Generated from url.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .urlParser import urlParser
else:
    from urlParser import urlParser

import random


# This class defines a complete listener for a parse tree produced by urlParser.
class urlListener(ParseTreeListener):

    # Enter a parse tree produced by urlParser#url.
    def enterUrl(self, ctx:urlParser.UrlContext):
        pass

    # Exit a parse tree produced by urlParser#url.
    def exitUrl(self, ctx:urlParser.UrlContext):
        pass


    # Enter a parse tree produced by urlParser#uri.
    def enterUri(self, ctx:urlParser.UriContext):
        pass

    # Exit a parse tree produced by urlParser#uri.
    def exitUri(self, ctx:urlParser.UriContext):
        pass


    # Enter a parse tree produced by urlParser#scheme.
    def enterScheme(self, ctx:urlParser.SchemeContext):
        pass

    # Exit a parse tree produced by urlParser#scheme.
    def exitScheme(self, ctx:urlParser.SchemeContext):
        pass


    # Enter a parse tree produced by urlParser#host.
    def enterHost(self, ctx:urlParser.HostContext):
        pass

    # Exit a parse tree produced by urlParser#host.
    def exitHost(self, ctx:urlParser.HostContext):
        pass


    # Enter a parse tree produced by urlParser#DomainNameOrIPv4Host.
    def enterDomainNameOrIPv4Host(self, ctx:urlParser.DomainNameOrIPv4HostContext):
        pass

    # Exit a parse tree produced by urlParser#DomainNameOrIPv4Host.
    def exitDomainNameOrIPv4Host(self, ctx:urlParser.DomainNameOrIPv4HostContext):
        pass


    # Enter a parse tree produced by urlParser#IPv4Host.
    def enterIPv4Host(self, ctx:urlParser.IPv4HostContext):
        pass

    # Exit a parse tree produced by urlParser#IPv4Host.
    def exitIPv4Host(self, ctx:urlParser.IPv4HostContext):
        pass


    # Enter a parse tree produced by urlParser#IPv6Host.
    def enterIPv6Host(self, ctx:urlParser.IPv6HostContext):
        pass

    # Exit a parse tree produced by urlParser#IPv6Host.
    def exitIPv6Host(self, ctx:urlParser.IPv6HostContext):
        pass


    # Enter a parse tree produced by urlParser#v4host.
    def enterV4host(self, ctx:urlParser.V4hostContext):
        pass

    # Exit a parse tree produced by urlParser#v4host.
    def exitV4host(self, ctx:urlParser.V4hostContext):
        pass


    # Enter a parse tree produced by urlParser#v6host.
    def enterV6host(self, ctx:urlParser.V6hostContext):
        pass

    # Exit a parse tree produced by urlParser#v6host.
    def exitV6host(self, ctx:urlParser.V6hostContext):
        pass


    # Enter a parse tree produced by urlParser#port.
    def enterPort(self, ctx:urlParser.PortContext):
        pass

    # Exit a parse tree produced by urlParser#port.
    def exitPort(self, ctx:urlParser.PortContext):
        pass


    # Enter a parse tree produced by urlParser#path.
    def enterPath(self, ctx:urlParser.PathContext):
        pass

    # Exit a parse tree produced by urlParser#path.
    def exitPath(self, ctx:urlParser.PathContext):
        pass


    # Enter a parse tree produced by urlParser#user.
    def enterUser(self, ctx:urlParser.UserContext):
        pass

    # Exit a parse tree produced by urlParser#user.
    def exitUser(self, ctx:urlParser.UserContext):
        pass


    # Enter a parse tree produced by urlParser#login.
    def enterLogin(self, ctx:urlParser.LoginContext):
        pass

    # Exit a parse tree produced by urlParser#login.
    def exitLogin(self, ctx:urlParser.LoginContext):
        pass


    # Enter a parse tree produced by urlParser#password.
    def enterPassword(self, ctx:urlParser.PasswordContext):
        pass

    # Exit a parse tree produced by urlParser#password.
    def exitPassword(self, ctx:urlParser.PasswordContext):
        pass


    # Enter a parse tree produced by urlParser#frag.
    def enterFrag(self, ctx:urlParser.FragContext):
        pass

    # Exit a parse tree produced by urlParser#frag.
    def exitFrag(self, ctx:urlParser.FragContext):
        pass


    # Enter a parse tree produced by urlParser#query.
    def enterQuery(self, ctx:urlParser.QueryContext):
        pass

    # Exit a parse tree produced by urlParser#query.
    def exitQuery(self, ctx:urlParser.QueryContext):
        pass


    # Enter a parse tree produced by urlParser#search.
    def enterSearch(self, ctx:urlParser.SearchContext):
        pass

    # Exit a parse tree produced by urlParser#search.
    def exitSearch(self, ctx:urlParser.SearchContext):
        pass


    # Enter a parse tree produced by urlParser#searchparameter.
    def enterSearchparameter(self, ctx:urlParser.SearchparameterContext):
        pass

    # Exit a parse tree produced by urlParser#searchparameter.
    def exitSearchparameter(self, ctx:urlParser.SearchparameterContext):
        pass


    # Enter a parse tree produced by urlParser#string.
    def enterString(self, ctx:urlParser.StringContext):
        pass

    # Exit a parse tree produced by urlParser#string.
    def exitString(self, ctx:urlParser.StringContext):
        pass



del urlParser