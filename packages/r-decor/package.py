# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecor(RPackage):
    """Retrieve Code Decorations
    
    Retrieves code comment decorations for C++ languages of the form '\\ [[xyz]]', which are used for automated wrapping of C++ functions.
    """

    homepage = "https://github.com/r-lib/decor"
    cran = "decor"


    version("1.0.2", sha256="2e6c0cf3804253298c43c7cc64e389cf0ef2bebdca18753a487b9861e54671f6")

    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))

