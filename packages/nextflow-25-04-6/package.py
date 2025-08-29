# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Nextflow25046(Package):
    """Nextflow is a data-driven computational pipeline framework that
    enables scalable and reproducible scientific workflows using software
    containers.

    This package installs the prebuilt launcher and JAR for Nextflow 25.04.6.
    """

    homepage = "https://www.nextflow.io"
    # Use the prebuilt shaded JAR ("one" packaging) for this specific release
    url = (
        "https://www.nextflow.io/releases/v25.04.6/nextflow-25.04.6-one.jar"
    )

    license("Apache-2.0")

    # Specific pinned version matching the package name
    version(
        "25.04.6",
        sha256="a03539c2a2369d7765995a1b5e6aef8a619a8989b17e73b915606c7a55631884",
        expand=False,
    )

    def url_for_version(self, version):
        # Always fetch the shaded "one" JAR for the specified version
        return f"https://www.nextflow.io/releases/v{version}/nextflow-{version}-one.jar"

    # Launcher script from the GitHub release assets
    resource(
        name="launcher",
        url="https://github.com/nextflow-io/nextflow/releases/download/v25.04.6/nextflow",
        sha256="a94f8bd1db9c0271ad58ec40b9c71f812d081a66f782396928b9b1f740f0be5f",
        expand=False,
        placement="launcher",
    )

    # Requires a Java runtime (Nextflow requires Java 17 or newer)
    depends_on("java@17:", type="run")

    def install(self, spec, prefix):
        # Install the launcher to bin
        mkdirp(prefix.bin)
        launcher_src = join_path(self.stage.source_path, "launcher", "nextflow")
        set_executable(launcher_src)
        install(launcher_src, join_path(prefix.bin, "nextflow"))

        # Install the JAR to a path that matches the launcher's expected layout:
        # $NXF_DIST/$NXF_VER/$NXF_JAR with NXF_PACK=one
        # We'll set NXF_DIST via environment to prefix.libexec/framework
        nxf_dist = join_path(prefix.libexec, "framework")
        nxf_ver_dir = join_path(nxf_dist, str(self.version))
        mkdirp(nxf_ver_dir)

        # The fetched file is the shaded JAR itself; use stage.archive_file
        jar_dst = join_path(nxf_ver_dir, f"nextflow-{self.version}-one.jar")
        install(self.stage.archive_file, jar_dst)

    def setup_run_environment(self, env):
        # Point Nextflow to the installed framework directory so it won't try to download
        env.set("NXF_DIST", join_path(self.prefix.libexec, "framework"))

    @run_after("install")
    def install_test(self):
        # Basic sanity check: ensure the launcher runs and reports version
        with working_dir("spack-test", create=True):
            import os

            exe = Executable(join_path(self.prefix.bin, "nextflow"))
            # Use the installed framework path and the packaged Java runtime
            env = {
                "NXF_DIST": join_path(self.prefix.libexec, "framework"),
                "JAVA_HOME": self.spec["java"].prefix,
                # Ensure a writable home for caches during test
                "NXF_HOME": os.getcwd(),
            }
            exe("-version", env=env)
