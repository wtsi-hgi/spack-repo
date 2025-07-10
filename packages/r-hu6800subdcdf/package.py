# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu6800subdcdf(RPackage):
	"""hu6800subdcdf

	A package containing an environment representing the Hu6800subD.CDF file.
	"""
	
	bioc = "hu6800subdcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu6800subdcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu6800subdcdf/hu6800subdcdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="dcdda9a0b0157976f58be91d1422e78234ee0414c6255850b7d6b9a2acf751b1")

	depends_on("r-annotationdbi", type=("build", "run"))

