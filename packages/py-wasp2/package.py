# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyWasp2(PythonPackage):
	"""Allele-specific analysis of next-generation sequencing data with high-performance multi-format variant support (VCF/cyvcf2/PGEN)"""
	
	homepage = "https://github.com/mcvickerlab/WASP2"
	pypi = "wasp2/wasp2-1.4.1.tar.gz" 

	version("1.3.0", sha256="e0b90e013cf86d1d1b651830c12677e4845be5e51e08fde39024a7e883f9c036")
	version("1.3.1", sha256="1baa9442e7d2b57e0887fba17b4ff472501d115ab4a78a23b0fe45175479c708")
	version("1.3.2", sha256="2e9499a32acf133da09402d17060919a1726ae54d1894e69a34d4e9fe521ac55")
	version("1.3.3", sha256="7e9f0f23426cdac056f3d26b16961c88189c1512b80b3b2ec5cdd9894195be8c")
	version("1.4.0", sha256="8d73c53290eb7df01cb297661a7ca968a43cc04d132f278422221d09606c440c")
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
