# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFastools(PythonPackage):
    """FASTA/FASTQ analysis and manipulation toolkit."""

    homepage = "https://pypi.org/project/fastools"
    pypi = "fastools/fastools-1.1.5.tar.gz"

    version("1.1.0", sha256="cab060fe43b3309b964ca4901a9c57275e85a9807c100fa9b3060b6e23dc7742")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

