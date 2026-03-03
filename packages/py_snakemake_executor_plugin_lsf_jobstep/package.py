# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySnakemakeExecutorPluginLsfJobstep(PythonPackage):
	"""A Snakemake executor plugin for running bjobs jobs inside of LSF jobs (meant for internal use by snakemake-executor-plugin-lsf)"""
	
	homepage = "https://github.com/BEFH/snakemake-executor-plugin-lsf-jobstep"
	pypi = "snakemake-executor-plugin-lsf-jobstep/snakemake_executor_plugin_lsf_jobstep-0.1.10" 

	version("0.1.10", sha256="e231e6e41649c528813133959536956a0a0d2b9d0a0bb76ad568d389b8ccba23", expand=False, url="https://files.pythonhosted.org/packages/48/ef/a5e169cbf32c1e677a1c6ab25210d4380cc6f09c4746f226e60798e6a446/snakemake_executor_plugin_lsf_jobstep-0.1.10-py3-none-any.whl")

	depends_on("python@3.11:", type=("build", "run"))
	depends_on("py-snakemake-interface-executor-plugins", type=("build", "run"))
	depends_on("py-snakemake-interface-common", type=("build", "run"))
