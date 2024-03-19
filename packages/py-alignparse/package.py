# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyAlignparse(PythonPackage):
    """Align long sequencing reads to targets, filter these alignments based on user-provided specifications, and parse out user-defined sequence features."""

    homepage = "https://jbloomlab.github.io/alignparse/index.html"
    git = "https://github.com/jbloomlab/alignparse/"
    pypi = "alignparse/alignparse-0.6.2.tar.gz"

    version("0.6.2", sha256="b508a79f93141e05e980bf58655d1ec97ff5ec3fc7e72f5b72f5d370616d6918")

    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    #depends_on("py-jupyterlab", type=("build", "run"))
    #depends_on("py-py-nbdime", type="build")

    depends_on("py-pandas@0.25.1:", type=("build", "run"))
    depends_on("py-numpy@1.17:", type=("build", "run"))
    depends_on("py-biopython@1.73:", type=("build", "run"))
    depends_on("py-matplotlib@3.0.0:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-pathos@0.2.4:", type=("build", "run"))
    depends_on("py-pysam@0.14:", type=("build", "run"))
    depends_on("py-scipy@1.2:", type=("build", "run"))
    depends_on("py-pyyaml@2.1.1:", type=("build", "run"))

    depends_on("py-plotnine@0.6:", type=("build", "run"))
    depends_on("py-palettable", type=("build", "run"))

    #depends_on("py-regex@2.5.33", type=("build", "run"))
    depends_on("py-regex", type=("build", "run"))
    
    depends_on("py-dna-features-viewer", type=("build", "run"))
    depends_on("minimap2", type=("build", "run"))
    depends_on("py-dms-variants", type=("build", "run"))

