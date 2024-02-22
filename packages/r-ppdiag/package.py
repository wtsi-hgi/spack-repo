# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpdiag(RPackage):
	"""Diagnosis and Visualizations Tools for Temporal Point Processes

	A suite of diagnostic tools for univariate point processes.
    This includes tools for simulating and fitting both common and more
    complex temporal point processes. We also include functions to 
    visualise these point processes and collect existing diagnostic
    tools of Brown et al. (2002) <doi:10.1162/08997660252741149> and
    Wu et al. (2021) <doi:10.1002/9781119821588.ch7>,
    which can be used to assess the fit of a chosen point process
    model.
	"""
	
	homepage = "https://owenward.github.io/ppdiag/"
	cran = "ppdiag" 

	version("0.1.1", md5="5d00a6aea33070672d27438d30de7578")

	depends_on("r@3.5:", type=("build", "run"))
