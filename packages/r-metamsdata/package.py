# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetamsdata(RPackage):
	"""Example CDF data for the metaMS package

	Example CDF data for the metaMS package
	"""
	
	bioc = "metaMSdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/metaMSdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/metaMSdata/metaMSdata_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="2d348466dde7a92eb55dec99e612e876df9fe882d96c95c693fb7f80a6ecf1a1")


