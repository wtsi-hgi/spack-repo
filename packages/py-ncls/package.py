# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNcls(PythonPackage):
    """A fast interval tree-like implementation in C, wrapped for the Python 
    ecosystem."""

    git = "https://github.com/pyranges/ncls"

    version("0.0.68", sha256="1b25c1f8f208f8b0a631165d6ae0468287054507")
    
    depends_on("py-numpy", type=("build", "run"))
