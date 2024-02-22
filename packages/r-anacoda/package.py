# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnacoda(RPackage):
	"""Analysis of Codon Data under Stationarity using a Bayesian
Framework

	Is a collection of models to analyze genome scale codon
        data using a Bayesian framework. Provides visualization
        routines and checkpointing for model fittings. Currently
        published models to analyze gene data for selection on codon
        usage based on Ribosome Overhead Cost (ROC) are: ROC (Gilchrist
        et al. (2015) <doi:10.1093/gbe/evv087>), and ROC with phi
        (Wallace & Drummond (2013) <doi:10.1093/molbev/mst051>). In
        addition 'AnaCoDa' contains three currently unpublished models.
        The FONSE (First order approximation On NonSense Error) model
        analyzes gene data for selection on codon usage against of
        nonsense error rates. The PA (PAusing time) and PANSE (PAusing
        time + NonSense Error) models use ribosome footprinting data to
        analyze estimate ribosome pausing times with and without
        nonsense error rate from ribosome footprinting data.
	"""
	
	homepage = "https://github.com/clandere/AnaCoDa"
	cran = "AnaCoDa" 

	version("0.1.4.4", md5="1156807f2128bd4772e4b9df9559c5b9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
