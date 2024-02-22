# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDae(RPackage):
	"""Functions Useful in the Design and ANOVA of Experiments

	The content falls into the following groupings: (i) Data, (ii)
    Factor manipulation functions, (iii) Design functions, (iv) ANOVA functions, (v)
    Matrix functions, (vi) Projector and canonical efficiency functions, and (vii)
    Miscellaneous functions. There is a vignette describing how to use the 
    design functions for randomizing and assessing designs available as a 
    vignette called 'DesignNotes'. The ANOVA functions facilitate the extraction of 
    information when the 'Error' function has been used in the call to 'aov'. 
    The package 'dae' can also be installed from 
  <http://chris.brien.name/rpackages/>.
	"""
	
	homepage = "http://chris.brien.name"
	cran = "dae" 

	version("3.2.21", md5="c6d97105faf05d4ce1e26cd45cbf8342")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
