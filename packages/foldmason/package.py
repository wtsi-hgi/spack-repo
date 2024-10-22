# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Foldmason(CMakePackage):
    """FoldMason is a software tool for constructing accurate multiple alignments from large sets of protein structures."""

    homepage = "https://github.com/steineggerlab/foldmason"
    url = "https://github.com/steineggerlab/foldmason/archive/refs/tags/1-763a428.zip"

    version("1-763a428", sha256="6d257a63dfab1bc7b53b1422e1c59b6ea8369cd7091fcae1be6c78e8e134ef83")

    depends_on("rust", type="build")
