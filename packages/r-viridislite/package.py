# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RViridislite(RPackage):
    """Colorblind-Friendly Color Maps (Lite Version)

    Color maps designed to improve graph readability for readers with common forms of color blindness and/or color vision deficiency. The color maps are also perceptually-uniform, both in regular form and also when converted to black-and-white for printing. This is the 'lite' version of the 'viridis' package that also contains 'ggplot2' bindings for discrete and continuous color and fill scales and can be found at <https://cran.r-project.org/package=viridis>.
    """
    
    homepage = "https://sjmgarnier.github.io/viridisLite/"
    cran = "viridisLite"

    version("0.4.2", sha256="893f111d31deccd2cc959bc9db7ba2ce9020a2dd1b9c1c009587e449c4cce1a1")

