# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFscanr(RPackage):
	"""Detect Programmed Ribosomal Frameshifting Events from mRNA/cDNA BLASTX Output

	'FScanR' identifies Programmed Ribosomal Frameshifting (PRF) events from BLASTX homolog sequence alignment between targeted genomic/cDNA/mRNA sequences against the peptide library of the same species or a close relative. The output by BLASTX or diamond BLASTX will be used as input of 'FScanR' and should be in a tabular format with 14 columns. For BLASTX, the output parameter should be: -outfmt '6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qframe sframe'. For diamond BLASTX, the output parameter should be: -outfmt 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qframe qframe.
	"""
	
	bioc = "FScanR" 

	version("1.12.0", commit="7f57e66bee59ee2f83ff04c35827643b410dd60a")

	depends_on("r@4:", type=("build", "run"))
