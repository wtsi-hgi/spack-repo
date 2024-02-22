# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBraingraph(RPackage):
	"""Graph Theory Analysis of Brain MRI Data

	A set of tools for performing graph theory analysis of brain MRI
    data. It works with data from a Freesurfer analysis (cortical thickness,
    volumes, local gyrification index, surface area), diffusion tensor
    tractography data (e.g., from FSL) and resting-state fMRI data (e.g., from
    DPABI). It contains a graphical user interface for graph visualization and
    data exploration, along with several functions for generating useful
    figures.
	"""
	
	homepage = "https://github.com/cwatson/brainGraph"
	cran = "brainGraph" 

	version("3.0.0", md5="51114b8a34b77ceb1d31696afd04e9ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph@1.2.4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
