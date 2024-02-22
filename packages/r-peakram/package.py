# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeakram(RPackage):
	"""Monitor the Total and Peak RAM Used by an Expression or Function

	When working with big data sets, RAM conservation is critically
    important. However, it is not always enough to just monitor the
    size of the objects created. So-called "copy-on-modify" behavior,
    characteristic of R, means that some expressions or functions may
    require an unexpectedly large amount of RAM overhead. For example,
    replacing a single value in a matrix duplicates that matrix in the
    back-end, making this task require twice as much RAM as that used
    by the matrix itself. This package makes it easy to monitor the total
    and peak RAM used so that developers can quickly identify and
    eliminate RAM hungry code.
	"""
	
	homepage = "http://github.com/tpq/peakRAM"
	cran = "peakRAM" 

	version("1.0.2", md5="5c769d3a2aba40787ef90a650eee9fd3")

	depends_on("r@3.2.2:", type=("build", "run"))
