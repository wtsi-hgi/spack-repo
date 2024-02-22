# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpd(RPackage):
	"""Methods for Measuring Functional Diversity Based on Trait
Probability Density

	Tools to calculate trait probability density functions (TPD) at
    any scale (e.g. populations, species, communities). TPD functions are used to compute
    several indices of functional diversity, as well as its partition across scales.
    These indices constitute a unified framework that incorporates the underlying
    probabilistic nature of trait distributions into uni- or multidimensional
    functional trait-based studies. See Carmona et al. (2016) <doi:10.1016/j.tree.2016.02.003> for
    further information.
	"""
	
	cran = "TPD" 

	version("1.1.0", md5="7cf0235f06ed84aeb52b3907dc1fc35f")

	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-ks@1.9.2:", type=("build", "run"))
	depends_on("r-gridextra@0.9.1:", type=("build", "run"))
	depends_on("r-mvtnorm@0.8:", type=("build", "run"))
