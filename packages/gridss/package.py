# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class Gridss(MavenPackage):
    """GRIDSS: the Genomic Rearrangement IDentification Software Suite."""

    homepage = "https://github.com/PapenfussLab/gridss"
    url      = "https://github.com/PapenfussLab/gridss/archive/refs/tags/v2.13.2.tar.gz"
    list_url = "https://github.com/PapenfussLab/gridss/tags"

    license("GPL-3.0-only")

    version("2.13.2", sha256="011eaf017538c690b745eb2e4680e04487b89cbd10ae17060401a7c7200c4397")
    version("2.13.1", sha256="f80e64b10262f22c5ac8620ad3afce3ad82b8638428f3e3cd83044989c507a01")
    version("2.13.0", sha256="7dccb239a6845f292f19ad5a92a35e141e362b40435311d0af20fdeb57c9721a")
    version("2.12.2", sha256="ae63dbb015501150b1f05991e93172979658af291d27affb2a4504c27e502a43")
    version("2.12.1", sha256="375701600dbb35d9abe3eb6e3b4bc6bc17191cf01a0c73eb9044857aaa17bee5")
    version("2.12.0", sha256="815a9a01e11ede11c75800fed55db67a6363677894b2a1a668815a9cbce76b73")
    version("2.11.1", sha256="55ff0207aba8ce49c02efe66b026e9a41d08d3c5bc9c0ce097dbe6325d37be0a")
    version("2.11.0", sha256="a028954ba7206b034392f7b62f590d454e92eae5e81592aa8647f37c8292dd8c")
    version("2.10.2", sha256="119a2f963ace33639f92d888d39c02758c2dd64a9e12c61c8913df908dc08f56")
    version("2.10.1", sha256="3f8ac6f70cd849d096b801d46d7da2f16ec74fb437838d0bccadec551d3b0f7a")

    depends_on("java@8:", type=("build", "run"))
    depends_on("bwa", type="run")
    depends_on("samtools", type="run")

    def install(self, spec, prefix):
        # Build the JAR file
        mvn = which("mvn")
        mvn("clean", "package", "-DskipTests")
        
        # Create bin and lib directories
        mkdir(prefix.bin)
        mkdir(prefix.lib)
        
        # Find the built JAR file
        jar_pattern = "target/gridss-*-gridss-jar-with-dependencies.jar"
        jar_files = find(".", jar_pattern, recursive=True)
        if not jar_files:
            raise RuntimeError("GRIDSS JAR file not found after build")
        
        jar_file = jar_files[0]
        jar_name = os.path.basename(jar_file)
        
        # Install the JAR file with its proper name
        install(jar_file, join_path(prefix.lib, jar_name))
        
        # Create wrapper script
        script_path = join_path(prefix.bin, "gridss")
        with open(script_path, "w") as fh:
            fh.write("#!/bin/bash\n")
            fh.write("JAR=\"{}/lib/{}\"\n".format(prefix, jar_name))
            fh.write("if [[ ! -f \"$JAR\" ]]; then echo 'GRIDSS jar not found: $JAR'; exit 1; fi\n")
            fh.write("exec java -cp \"$JAR\" gridss.CallVariants \"$@\"\n")
        os.chmod(script_path, 0o755)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin) 