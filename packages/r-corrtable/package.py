# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrtable(RPackage):
	"""Creates and Saves Out a Correlation Table with Significance
Levels Indicated

	After using this, a publication-ready correlation table with p-values
  indicated will be created.  The input can be a full data frame; any
  string and Boolean terms will be dropped as part of functionality.  Correlations and
  p-values are calculated using the 'Hmisc' framework.  Output of the 
  correlation_matrix() function is a table of strings; this gets saved out to a '.csv2'
  with the save_correlation_matrix() function for easy insertion into a paper.
  For more details about the process, consult
  <https://paulvanderlaken.com/2020/07/28/publication-ready-correlation-matrix-significance-r/>.
	"""
	
	cran = "corrtable" 

	version("0.1.1", md5="80c52972f153f45d087700bc9cea0c7a")

	depends_on("r-hmisc", type=("build", "run"))
