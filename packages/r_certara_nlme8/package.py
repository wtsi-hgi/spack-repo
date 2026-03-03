# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCertaraNlme8(RPackage):
	"""Utilities for Certara's Nonlinear Mixed-Effects Modeling Engine

	Perform Nonlinear Mixed-Effects (NLME) Modeling using Certara's
    NLME-Engine. Access the same Maximum Likelihood engines used in the Phoenix
    platform, including algorithms for parametric methods, individual, and pooled
    data analysis <https://www.certara.com/app/uploads/2020/06/BR_PhoenixNLME-v4.pdf>.
    The Quasi-Random Parametric Expectation-Maximization Method (QRPEM) is also
    supported <https://www.page-meeting.org/default.asp?abstract=2338>. Execution
    is supported both locally or on remote machines. Remote execution includes
    support for Linux Sun Grid Engine (SGE), Terascale Open-source Resource and
    Queue Manager (TORQUE) grids, Linux and Windows multicore, and individual runs.
	"""
	
	cran = "Certara.NLME8" 

	version("1.2.4", md5="292a0a1536a1c85e729bcb77aefeeced", url="https://cran.r-project.org/src/contrib/Certara.NLME8_1.2.4.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-batchtools@0.9.9:", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
