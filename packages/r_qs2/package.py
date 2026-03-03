# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RQs2(RPackage):
    """qs2 is the successor to the qs package. The goal is to have reliable and fast performance for saving and loading objects in R."""


    license("GPL-3.0")

    cran="qs2"

    version("0.1.7", sha256="8a3f5229f68cbdfaec3db84afa992c7569dd327fdc6e07e5eff73c17502cfee8")
    version("0.1.6", sha256="ebc9b763d3c8d5e253e396138c62aad67d86ba15e36cd0e1f688a81a74ac3ade")
    version("0.1.5", sha256="ad0c1d27e6a021fe8c8f410169b140f953eb012b25e5b8cd11efe409536d031a")
    version("0.1.4", sha256="c2dec8a8643db08ae6e496fd775fe723aba86742d9fb3fc93b65aa640e162f04")
    version("0.1.3", sha256="5babebcfb2742426a498ed75bd3054d47901e14957768d92025d9713bb506585")
    version("0.1.2", sha256="bc41f270bf75716c0a0742a13880a2bbfeb9700aff3ff9593c06ecef4e27bffd")
    version("0.1.1", sha256="cce8f5a6e1dff7f73d39219240bdf9e6bfb8f1a8d98913a79d354fcb9a584529")

    depends_on("r@3.5.0:")
    depends_on("r-rcpp")
    depends_on("r-stringfish@0.18.0:")

  
