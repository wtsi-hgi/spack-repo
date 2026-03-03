# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDrop(PythonPackage):
    """The detection of RNA Outliers Pipeline (DROP) is an integrative workflow to detect aberrant expression, aberrant splicing, and mono-allelic expression from raw sequencing files."""

    homepage = "https://github.com/gagneurlab/drop"

    url = "https://github.com/gagneurlab/drop/archive/refs/tags/1.3.3.tar.gz"

    version("1.3.3", sha256="846d39e3e6f61e4dcc65c9e205040cb49b43b8a4790189dc225e027a9bf00917")
    version("1.3.2", sha256="aa5468f8f0091fe4a85464e5f85deaf39e4bbe5de76c33e2dd73e21101a9f2e5")
    version("1.3.1", sha256="8dd8aaabffa92ad96d956ade8126b6c06b1eef39159a31b676f85505706b9b9f")
    version("1.3.0", sha256="a3f418f37a7c6fb9714e8b2e84e57b5743cbcecb7ea46773ba805cf7de0e7c49")
    version("1.2.4", sha256="5fcfffb4b9a0160a45012ecc4e894726b514c957111d80daf4789d27d0cbcad1")
    version("1.2.3", sha256="56bdad81daf4a15e4f8818d157bb49603ccf2664325701b08a96098c764b9c2c")
    version("1.2.2", sha256="738879a432646c9bae0b9d8e5456f3b4b58ef450c385ecc61c0f08cacf16702d")
    version("1.2.1", sha256="101e023a338fa6e525aac6bad973723df8dd8736ecc6643aaaa8112b479153b5")
    version("1.2.0", sha256="ca062dc376e3f68eee36648614affc7bd5210d9f21a0dc9388bc41b52811bb04")
    version("1.1.4", sha256="0ea30a369a52db4426bdb05501e17939a670691ed17c6bce7b982d58127cf540")

    depends_on("py-wbuild@1.8.0:", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"))
    depends_on("py-pandoc", type=("build", "run"))
    depends_on("py-graphviz", type=("build", "run"))
    depends_on("py-pandas@0.13:", type=("build", "run"))
