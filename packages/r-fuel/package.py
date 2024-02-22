# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuel(RPackage):
	"""Framework for Unified Estimation in Lognormal Models

	Lognormal models have broad applications in various research areas such as economics, actuarial science, biology, environmental science and psychology. The estimation problem in lognormal models has been extensively studied. This R package 'fuel' implements thirty-nine existing and newly proposed estimators. See Zhang, F., and Gou, J. (2020), A unified framework for estimation in lognormal models, Technical report. 
	"""
	
	cran = "fuel" 

	version("1.2.0", md5="fec2ab41e6bd3c4f4e8e375e40776af1")

