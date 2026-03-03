# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComplexupset(RPackage):
	"""Create Complex UpSet Plots Using 'ggplot2' Components

	UpSet plots are an improvement over Venn Diagram for set overlap visualizations.
    Striving to bring the best of the 'UpSetR' and 'ggplot2', this package offers a way to create
    complex overlap visualisations, using simple and familiar tools, i.e. geoms of 'ggplot2'.
    For introduction to UpSet concept, see Lex et al. (2014) <doi:10.1109/TVCG.2014.2346248>.
	"""
	
	homepage = "https://github.com/krassowski/complex-upset"
	cran = "ComplexUpset" 

	version("1.3.3", md5="cabac9c2e5d8775011e8d8dae2fa49ea")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
