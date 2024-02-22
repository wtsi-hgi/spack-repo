# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPinfsc50(RPackage):
	"""Sequence ('FASTA'), Annotation ('GFF') and Variants ('VCF') for 17
	Samples of 'P. Infestans" and 1 'P. Mirabilis'.

	Genomic data for the plant pathogen "Phytophthora infestans." It includes a
	variant file ('VCF'), a sequence file ('FASTA') and an annotation file
	('GFF'). This package is intended to be used as example data for packages
	that work with genomic data."""

	cran = "pinfsc50"

	maintainers("dorton21")

	version("1.3.0", md5="ec89a5a85a4c8975899b704b19acc1cb", url="https://cran.r-project.org/src/contrib/pinfsc50_1.3.0.tar.gz")

	depends_on("r@3.2.1:", type=("build", "run"))
