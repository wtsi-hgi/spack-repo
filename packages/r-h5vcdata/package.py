# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH5vcdata(RPackage):
	"""Example data for the h5vc package

	This package contains the data used in the vignettes and examples of the 'h5vc' package
	"""
	
	bioc = "h5vcData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/h5vcData_2.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/h5vcData/h5vcData_2.22.0.tar.gz"]

	version("2.22.0", sha256="ff015754b692f4057063e947d01e76a1bfa6c9715f71b4123f3c2a6f1eced45d")


