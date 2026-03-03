# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttk(RPackage):
	"""High-Throughput Toxicokinetics

	Pre-made models that can be rapidly tailored to various chemicals
             and species using chemical-specific in vitro data and physiological 
             information. These tools allow incorporation of chemical 
             toxicokinetics ("TK") and in vitro-in vivo extrapolation ("IVIVE") 
             into bioinformatics, as described by Pearce et al. (2017) 
             (<doi:10.18637/jss.v079.i04>). Chemical-specific 
             in vitro data characterizing toxicokinetics have been obtained 
             from relatively high-throughput experiments.   The 
             chemical-independent ("generic") physiologically-based ("PBTK") and empirical 
             (for example, one compartment) "TK" models included here can be 
             parameterized with in vitro data or in silico predictions which are 
             provided for thousands of chemicals, multiple exposure routes, 
             and various species. High throughput toxicokinetics ("HTTK") is the 
             combination of in vitro data and generic models. We establish the
             expected accuracy of HTTK for chemicals without in vivo data 
             through statistical evaluation of HTTK predictions for chemicals
             where in vivo data do exist. The models are systems of ordinary 
             differential equations that are developed in MCSim and solved
             using compiled (C-based) code for speed. A Monte Carlo sampler is
             included for simulating human biological variability
             (Ring et al., 2017 <doi:10.1016/j.envint.2017.06.004>)
             and propagating parameter uncertainty 
             (Wambaugh et al., 2019 <doi:10.1093/toxsci/kfz205>). 
             Empirically calibrated methods are included for predicting 
             tissue:plasma partition coefficients and volume of distribution  
             (Pearce et al., 2017 <doi:10.1007/s10928-017-9548-7>).
             These functions and data provide a set of tools for using IVIVE to
             convert concentrations from high-throughput screening experiments
             (for example, Tox21, ToxCast) to real-world exposures via reverse 
             dosimetry (also known as "RTK")
             (Wetmore et al., 2015 <doi:10.1093/toxsci/kfv171>).
	"""
	
	homepage = "https://www.epa.gov/chemical-research/rapid-chemical-exposure-and-dose-research"
	cran = "httk" 

	version("2.3.1", md5="faf1d6819033f9a017f1012982755a24")
	version("2.3.0", md5="2b47e41bdca3f56a33c860b132b1af9a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
