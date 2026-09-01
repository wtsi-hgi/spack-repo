# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqarray(RPackage):
	"""Data Management of Large-Scale Whole-Genome Sequence Variant Calls

	Data management of large-scale whole-genome sequencing variant calls with thousands of individuals: genotypic data (e.g., SNVs, indels and structural variation calls) and annotations in SeqArray GDS files are stored in an array-oriented and compressed manner, with efficient data access using the R programming language.
	"""
	
	homepage = "https://github.com/zhengxwen/SeqArray"
	bioc = "SeqArray" 
	git = "https://git.bioconductor.org/packages/SeqArray"

	version("1.53.2", commit="49fb7f23a913354441e32099708c55746286840e")
	version("1.42.3", commit="ceb8c36c7098d179d43f8bae423cf8632756e438")
	version("1.42.2", commit="2f9f929eb78f1df990b390a813de0c2907e12616")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-digest", when="@1.53.2:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-seqinfo", when="@1.53.2:", type=("build", "run"))

	def patch(self):
		if self.spec.satisfies("@1.42.3:"):
			path = "src/vectorization.cpp"
		if self.spec.satisfies("@1.42.2"):
			path = "src/vectorization.c"
		filter_file("const __m256i mask3 = _mm256_set1_epi8('\\n');", "", path, string=True)
		filter_file("const __m256i mask4 = _mm256_set1_epi8('\\r');", "", path, string=True)
		filter_file("const __m128i mask2 = _mm_set1_epi8('\\r');", "const __m128i mask2 = _mm_set1_epi8('\\r');const __m256i mask3 = _mm256_set1_epi8('\\n');const __m256i mask4 = _mm256_set1_epi8('\\r');", path, string=True)
