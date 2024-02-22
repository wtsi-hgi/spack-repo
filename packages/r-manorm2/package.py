# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManorm2(RPackage):
	"""Tools for Normalizing and Comparing ChIP-seq Samples

	Chromatin immunoprecipitation followed by high-throughput
    sequencing (ChIP-seq) is the premier technology for profiling genome-wide
    localization of chromatin-binding proteins, including transcription
    factors and histones with various modifications.
    This package provides a robust method for normalizing ChIP-seq
    signals across individual samples or groups of samples. It also designs
    a self-contained system of statistical models for calling differential
    ChIP-seq signals between two or more biological conditions as well as
    for calling hypervariable ChIP-seq signals across samples. Refer to
    Tu et al. (2021) <doi:10.1101/gr.262675.120> and
    Chen et al. (2022) <doi:10.1186/s13059-022-02627-9>
    for associated statistical details.
	"""
	
	homepage = "https://github.com/tushiqi/MAnorm2"
	cran = "MAnorm2" 

	version("1.2.2", md5="b82edf2d8f183461a886db599173a865", url="https://cran.r-project.org/src/contrib/MAnorm2_1.2.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-locfit@1.5.9:", type=("build", "run"))
	depends_on("r-scales@0.3:", type=("build", "run"))
	depends_on("r-statmod@1.4.34:", type=("build", "run"))
