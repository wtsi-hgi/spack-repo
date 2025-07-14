# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebrafishrnaseq(RPackage):
	"""Zebrafish RNA-Seq Experimental Data from Ferreira et al. (2014)

	Gene-level read counts from RNA-Seq for gallein-treated and control zebrafish.
	"""
	
	bioc = "zebrafishRNASeq"

	version("1.28.0", commit="572433216119f1d7bda8f678cdb05f04a9b7cdc8")
	version("1.22.0", commit="15abb4d799b8b64807cb2ab2bdb3406ebd9ca7df")

	depends_on("r@2.10:", type=("build", "run"))

