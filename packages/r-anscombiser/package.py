# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnscombiser(RPackage):
	"""Create Datasets with Identical Summary Statistics

	Anscombe's quartet are a set of four two-variable datasets that 
    have several common summary statistics but which have very different joint 
    distributions.  This becomes apparent when the data are plotted, which 
    illustrates the importance of using graphical displays in Statistics.  This
    package enables the creation of datasets that have identical marginal sample
    means and sample variances, sample correlation, least squares regression 
    coefficients and coefficient of determination.  The user supplies an initial 
    dataset, which is shifted, scaled and rotated in order to achieve target 
    summary statistics.  The general shape of the initial dataset is retained. 
    The target statistics can be supplied directly or calculated based on a 
    user-supplied dataset.  The 'datasauRus' package 
    <https://cran.r-project.org/package=datasauRus> provides further examples 
    of datasets that have markedly different scatter plots but share many 
    sample summary statistics.
	"""
	
	homepage = "https://paulnorthrop.github.io/anscombiser/"
	cran = "anscombiser" 

	version("1.1.0", md5="9c70e7dc6757c8de7b7d72de76238130")

	depends_on("r@3.3:", type=("build", "run"))
