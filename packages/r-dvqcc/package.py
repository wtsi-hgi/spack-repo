# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDvqcc(RPackage):
	"""Dynamic VAR - Based Control Charts for Batch Process Monitoring

	A set of control charts for batch processes based on the VAR model. The package contains the implementation of T2.var and W.var control charts based on VAR model coefficients using the couple vectors theory. In each time-instant the VAR coefficients are estimated from a historical in-control dataset and a decision rule is made for online classifying of a new batch data. Those charts allow efficient online monitoring since the very first time-instant. The offline version is available too. In order to evaluate the chart's performance, this package contains functions to generate batch data for offline and online monitoring.See in Danilo Marcondes Filho and Marcio Valk (2020) <doi:10.1016/j.ejor.2019.12.038>. 
	"""
	
	cran = "dvqcc" 

	version("0.1.0", md5="504941ffafdf15189b754db7049f8139")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tsdyn", type=("build", "run"))
