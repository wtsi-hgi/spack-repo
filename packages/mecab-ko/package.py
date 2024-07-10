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
#     spack install mecab-ko
#
# You can edit this file again by typing:
#
#     spack edit mecab-ko
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class MecabKo(AutotoolsPackage):
    """The 'mecab-ko' and 'mecab-ko-dic' is based on a C++ library,
    and part-of-speech tagging with them is useful when the spacing of source Korean text is not correct.
    This package provides part-of-speech tagging and tokenization function for Korean text"""

    homepage = "https://bitbucket.org/eunjeon/mecab-ko/src/master/"
    url = "https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz"

    license("LGPL")

    version(
        "0.9.2",
        sha256="d0e0f696fc33c2183307d4eb87ec3b17845f90b81bf843bd0981e574ee3c38cb",
        url="https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz",
    )

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
