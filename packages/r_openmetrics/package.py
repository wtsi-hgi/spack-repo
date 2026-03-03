# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenmetrics(RPackage):
	"""A 'Prometheus' Client for R Using the 'OpenMetrics' Format

	Provides a client for the open-source monitoring and alerting
  toolkit, 'Prometheus', that emits metrics in the 'OpenMetrics' format. Allows
  users to automatically instrument 'Plumber' and 'Shiny' applications, collect
  standard process metrics, as well as define custom counter, gauge, and
  histogram metrics of their own.
	"""
	
	homepage = "https://github.com/atheriel/openmetrics"
	cran = "openmetrics" 

	version("0.3.0", md5="1d3503d8a881988cfea1eb90005b9d70")

	depends_on("r-r6", type=("build", "run"))
