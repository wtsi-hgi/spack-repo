# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHelixvis(RPackage):
	"""Visualize Alpha-Helical Peptide Sequences

	Create publication-quality, 2-dimensional visualizations of alpha-helical peptide
  sequences. Specifically, allows the user to programmatically generate
  helical wheels and wenxiang diagrams to provide a bird's eye, top-down view of
  alpha-helical oligopeptides. See Wadhwa RR, et al. (2018)
  <doi:10.21105/joss.01008> for more information.
	"""
	
	homepage = "https://github.com/rrrlw/helixvis"
	cran = "helixvis" 

	version("1.0.1", md5="5740c1dea2599aa3ce9a114ff8296d29")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-ggforce@0.1.3:", type=("build", "run"))
	depends_on("r-rlang@0.2.2:", type=("build", "run"))
