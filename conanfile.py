#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostPoly_CollectionConan(base.BoostBaseConan):
    name = "boost_poly_collection"
    url = "https://github.com/bincrafters/conan-boost_poly_collection"
    lib_short_names = ["poly_collection"]
    header_only_libs = ["poly_collection"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_iterator",
        "boost_mpl",
        "boost_type_erasure",
        "boost_type_traits"
    ]


