# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyWasp2(PythonPackage):
	"""Allele-specific analysis of next-generation sequencing data with high-performance multi-format variant support (VCF/cyvcf2/PGEN)"""
	
	homepage = "https://github.com/mcvickerlab/WASP2"
	pypi = "wasp2/wasp2-1.4.1.tar.gz" 

	version("1.4.1", sha256="801a3266f0e81fe6df2fd00a71deac3e58310ee2a6cc45ca3513b596ebe872ef")

	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-polars", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pysam", type=("build", "run"))
	depends_on("py-pybedtools", type=("build", "run"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-scanpy", type=("build", "run"))
	depends_on("py-typer", type=("build", "run"))
	depends_on("py-rich", type=("build", "run"))
	depends_on("samtools", type=("build", "run"))
	depends_on("bcftools", type=("build", "run"))
	depends_on("bedtools2", type=("build", "run"))
	depends_on("py-maturin", type="build")
	depends_on("cmake", type="build")
	depends_on("llvm+clang", type="build")

	@run_after("install")
	def install_test(self):
		with working_dir("spack-test", create=True):
			python("-c", "import wasp2")
