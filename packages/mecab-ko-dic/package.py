# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mecab-ko-dic
#
# You can edit this file again by typing:
#
#     spack edit mecab-ko-dic
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class MecabKoDic(AutotoolsPackage):
    """The 'mecab-ko' and 'mecab-ko-dic' is based on a C++ library,
    and part-of-speech tagging with them is useful when the spacing of source Korean text is not correct.
    This package provides part-of-speech tagging and tokenization function for Korean text"""

    homepage = "https://bitbucket.org/eunjeon/mecab-ko-dic/src/master/"
    url = "https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz"

    version("2.1.1-20180720", sha256="fd62d3d6d8fa85145528065fabad4d7cb20f6b2201e71be4081a4e9701a5b330")

    depends_on("mecab-ko")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        make("install", "DESTDIR={0}".format(prefix.bin))
