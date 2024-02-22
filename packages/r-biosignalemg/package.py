# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiosignalemg(RPackage):
	"""Tools for Electromyogram Signals (EMG) Analysis

	Data processing tools to compute the rectified, integrated and the averaged EMG. Routines for automatic detection of activation phases. A routine to compute and plot the ensemble average of the EMG. An EMG signal simulator for general purposes.
	"""
	
	cran = "biosignalEMG" 

	version("2.1.0", md5="9eb4065ec59b47a939b6c352c1d3af51")

	depends_on("r-signal", type=("build", "run"))
