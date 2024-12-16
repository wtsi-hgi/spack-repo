# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import pathlib

from spack.package import *


class GuacamoleClient(MavenPackage):
    """Apache Guacamole is a clientless remote desktop gateway. It
    supports standard protocols like VNC, RDP, and SSH."""

    homepage = "https://guacamole.apache.org/"
    url = "https://github.com/apache/guacamole-client/archive/1.2.0.tar.gz"

    license("Apache-2.0")

    version("1.5.5", sha256="ebbd3c0b73ddafbf6656d11324163f5b8d410f94b472791e6fa75fca13a5d30b")

    # remove usage of deprecated AccessController class, deprecated in java 17
    patch(
        "https://github.com/apache/guacamole-client/commit/b315e6aac84550948763a2bc99f12ceb2a28dca1.patch?full_index=1",
        sha256="3529eb8bfd3d025682463cbce3f5a58bdbcacfa58c915c5471e00913c89f7474",
        when="@1.5:1.5.5",
    )

    depends_on("java@8:", type=("build", "run"))
    depends_on("java@:16", type=("build", "run"), when="@:1.4")
    depends_on("tomcat", type="run")

    def build_args(self):
        # The file .spack_patched is flagged as an unapproved license
        return ["-Drat.numUnapprovedLicenses=1"]

    def setup_run_environment(self, env):
        war_file = pathlib.Path(self.prefix.guacamole.target).glob("*.war").pop()
        os.symlink(join_path(os.environ["CATALINA_HOME"] + "/webapps/guacamole.war"), war_file)
