# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtern(RPackage):
	"""An Extension to 'ggplot2', for the Creation of Ternary Diagrams

	Extends the functionality of 'ggplot2', providing the capability
    to plot ternary diagrams for (subset of) the 'ggplot2' geometries. Additionally,
    'ggtern' has implemented several NEW geometries which are unavailable to the
    standard 'ggplot2' release. For further examples and documentation, please
    proceed to the 'ggtern' website.
	"""
	
	homepage = "http://www.ggtern.com"
	cran = "ggtern" 

	version("3.5.0", md5="4468c59e1ba6ade63440e2ce549e9047")
	version("3.4.2", md5="3b92173f413640500e92a58184b18023")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-compositions@2.0.2:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-gtable@0.1.2:", type=("build", "run"))
	depends_on("r-latex2exp@0.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-scales@1.3:", type=("build", "run"))
	depends_on("r-proto@1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-hexbin@1.28.2:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
