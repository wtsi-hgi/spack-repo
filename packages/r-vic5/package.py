# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVic5(RPackage):
	"""The Variable Infiltration Capacity (VIC) Hydrological Model

	The Variable Infiltration Capacity (VIC) model is a macroscale
    hydrologic model that solves full water and energy balances, originally
    developed by Xu Liang at the University of Washington (UW).
    The version of VIC source code used is of 5.0.1 on <https://github.com/UW-Hydro/VIC/>,
    see Hamman et al. (2018).
    Development and maintenance of the current official version
    of the VIC model at present is led by the UW Hydro (Computational Hydrology
    group) in the Department of Civil and Environmental Engineering at UW. VIC is
    a research model and in its various forms it has been applied to most of the
    major river basins around the world, as well as globally 
    <http://vic.readthedocs.io/en/master/Documentation/References/>. 
    References: "Liang, X., D. P. Lettenmaier, E. F. Wood, and
    S. J. Burges (1994), A simple hydrologically based model of land surface water
    and energy fluxes for general circulation models, J. Geophys. Res., 99(D7),
    14415-14428, <doi:10.1029/94JD00483>"; 
    "Hamman, J. J., Nijssen, B., Bohn, T. J., Gergel, D. R., and Mao, Y. (2018), The
    Variable Infiltration Capacity model version 5 (VIC-5): infrastructure improvements
    for new applications and reproducibility, Geosci. Model Dev., 11, 3481-3496, 
    <doi:10.5194/gmd-11-3481-2018>".
	"""
	
	homepage = "https://github.com/rpkgs/VIC5"
	cran = "VIC5" 

	version("0.2.6", md5="75ac651ab76afebbba181f7714f04ad7", url="https://cran.r-project.org/src/contrib/VIC5_0.2.6.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
