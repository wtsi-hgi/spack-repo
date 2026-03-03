# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnaqcd(RPackage):
	"""Micro-RNA Quality Control and Diagnosis

	A complete and dedicated analytical toolbox for quality control and diagnosis based on subject-related measurements of micro-RNA (miRNA) expressions. The package consists of a set of functions that allow to train, optimize and use a Bayesian classifier that relies on multiplets of measured miRNA expressions. The package also implements the quality control tools required to preprocess input datasets. In addition, the package provides a function to carry out a statistical analysis of miRNA expressions, which can give insights to improve the classifier's performance. The method implemented in the package was first introduced in L. Ricci, V. Del Vescovo, C. Cantaloni, M. Grasso, M. Barbareschi and M. A. Denti, "Statistical analysis of a Bayesian classifier based on the expression of miRNAs", BMC Bioinformatics 16:287, 2015 <doi:10.1186/s12859-015-0715-9>. The package is thoroughly described in M. Castelluzzo, A. Perinelli, S. Detassis, M. A. Denti and L. Ricci, "MiRNA-QC-and-Diagnosis: An R package for diagnosis based on MiRNA expression", SoftwareX 12:100569, 2020 <doi:10.1016/j.softx.2020.100569>. Please cite both these works if you use the package for your analysis. DISCLAIMER: The software in this package is for general research purposes only and is thus provided WITHOUT ANY WARRANTY. It is NOT intended to form the basis of clinical decisions. Please refer to the GNU General Public License 3.0 (GPLv3) for further information.
	"""
	
	cran = "MiRNAQCD" 

	version("1.1.3", md5="b4a3c72d3c841dbc8d36366e5bf6bd9a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
