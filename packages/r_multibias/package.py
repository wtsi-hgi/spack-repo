# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultibias(RPackage):
	"""Simultaneous Multi-Bias Adjustment

	Quantify the causal effect of a binary exposure on a binary
    outcome with adjustment for multiple biases. The functions can
    simultaneously adjust for any combination of uncontrolled confounding,
    exposure/outcome misclassification, and selection bias.
    The underlying method generalizes the concept of combining inverse
    probability of selection weighting with predictive value weighting.
    Simultaneous multi-bias analysis can be used to enhance the validity
    and transparency of real-world evidence obtained from observational,
    longitudinal studies. Based on the work from Paul Brendel, Aracelis Torres,
    and Onyebuchi Arah (2023) <doi:10.1093/ije/dyad001>.
	"""
	
	homepage = "https://github.com/pcbrendel/multibias"
	cran = "multibias" 

	version("1.4.0", md5="9c01cd47b0c2796996b964b5ec03271c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.1.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
