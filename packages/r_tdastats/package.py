# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdastats(RPackage):
	"""Pipeline for Topological Data Analysis

	A comprehensive toolset for any
    useR conducting topological data analysis, specifically via the
    calculation of persistent homology in a Vietoris-Rips complex.
    The tools this package currently provides can be conveniently split
    into three main sections: (1) calculating persistent homology; (2)
    conducting statistical inference on persistent homology calculations;
    (3) visualizing persistent homology and statistical inference.
    The published form of TDAstats can be found in Wadhwa et al. (2018)
    <doi:10.21105/joss.00860>.   
    For a general background on computing persistent homology for
    topological data analysis, see Otter et al. (2017)
    <doi:10.1140/epjds/s13688-017-0109-5>.
    To learn more about how the permutation test is used for
    nonparametric statistical inference in topological data analysis,
    read Robinson & Turner (2017) <doi:10.1007/s41468-017-0008-7>.
    To learn more about how TDAstats calculates persistent homology,
    you can visit the GitHub repository for Ripser, the software that
    works behind the scenes at <https://github.com/Ripser/ripser>.
    This package has been published as Wadhwa et al. (2018)
    <doi:10.21105/joss.00860>.
	"""
	
	homepage = "https://github.com/rrrlw/TDAstats"
	cran = "TDAstats" 

	version("0.4.1", md5="7dc1bf32293229a523b34e76346b0cb3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
