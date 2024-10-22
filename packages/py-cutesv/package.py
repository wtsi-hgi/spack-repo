# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCutesv(PythonPackage):
    """Long-read sequencing enables the comprehensive discovery of structural variations (SVs). However, it is still non-trivial to achieve high sensitivity and performance simultaneously due to the complex SV characteristics implied by noisy long reads. Therefore, we propose cuteSV, a sensitive, fast and scalable long-read-based SV detection approach. cuteSV uses tailored methods to collect the signatures of various types of SVs and employs a clustering-and-refinement method to analyze the signatures to implement sensitive SV detection. Benchmarks on real Pacific Biosciences (PacBio) and Oxford Nanopore Technology (ONT) datasets demonstrate that cuteSV has better yields and scalability than state-of-the-art tools."""

    homepage = "https://github.com/tjiangHIT/cuteSV"
    pypi = "cuteSV/cuteSV-2.1.1.tar.gz"

    version("2.1.1", sha256="af4c50a3d0091275a09e50a025047fdf1afc7f8df5c98cf9ab27ea0ea559bc70")

    depends_on("python@3:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-cigar", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pyvcf3", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
