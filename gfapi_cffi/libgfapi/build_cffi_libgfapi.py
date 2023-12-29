from os import path

from cffi import FFI

glfs_c_header_source = r"""
#include <glusterfs/api/glfs.h>
"""

glfs_cdef = r"""
typedef struct glfs glfs_t;
typedef struct glfs_fd glfs_fd_t;

/* "..." - The cffi compiler will figure it out */
typedef int... dev_t;
typedef int... ino_t;
typedef int... mode_t;
typedef int... nlink_t;
typedef int... uid_t;
typedef int... gid_t;
typedef int... off_t;
typedef int... blksize_t;
typedef int... blkcnt_t;
typedef int... time_t;
typedef int... size_t;
typedef int... ssize_t;
typedef int... fsblkcnt_t;
typedef int... fsfilcnt_t;


/* "..." - The cffi compiler will use the header to fix the order of fields and size of the structure */
struct stat {
    dev_t     st_dev;     /* ID of device containing file */
    ino_t     st_ino;     /* inode number */
    mode_t    st_mode;    /* protection */
    nlink_t   st_nlink;   /* number of hard links */
    uid_t     st_uid;     /* user ID of owner */
    gid_t     st_gid;     /* group ID of owner */
    dev_t     st_rdev;    /* device ID (if special file) */
    off_t     st_size;    /* total size, in bytes */
    blksize_t st_blksize; /* blocksize for file system I/O */
    blkcnt_t  st_blocks;  /* number of 512B blocks allocated */
    time_t    st_atime;   /* time of last access */
    time_t    st_mtime;   /* time of last modification */
    time_t    st_ctime;   /* time of last status change */
    ...;
};

struct dirent {
    char d_name[256];
    ...;
};

struct statvfs {
    unsigned long  f_bsize;    /* file system block size */
    unsigned long  f_frsize;   /* fragment size */
    fsblkcnt_t     f_blocks;   /* size of fs in f_frsize units */
    fsblkcnt_t     f_bfree;    /* free blocks */
    fsblkcnt_t     f_bavail;   /* free blocks for unprivileged users */
    fsfilcnt_t     f_files;    /* inodes */
    fsfilcnt_t     f_ffree;    /* free inodes */
    fsfilcnt_t     f_favail;   /* free inodes for unprivileged users */
    unsigned long  f_fsid;     /* file system ID */
    unsigned long  f_flag;     /* mount flags */
    unsigned long  f_namemax;  /* maximum filename length */
    ...;
};

struct timespec {
    time_t   tv_sec;        /* seconds */
    long     tv_nsec;       /* nanoseconds */
};


glfs_t *glfs_new(const char *volname);  //3.4.0

int glfs_set_volfile_server(glfs_t *fs, const char *transport, const char *host, int port);  //3.4.0

int glfs_set_logging(glfs_t *fs, const char *logfile, int loglevel);  //3.4.0

int glfs_init(glfs_t *fs);  //3.4.0

int glfs_fini(glfs_t *fs);  //3.4.0

int glfs_get_volumeid(glfs_t *fs, char *volid, size_t size);  //3.5.0

int glfs_setfsuid(uid_t fsuid);  //3.4.2

int glfs_setfsgid(gid_t fsgid);  //3.4.2

glfs_fd_t * glfs_open(glfs_t *fs, const char *path, int flags);  //3.4.0

glfs_fd_t * glfs_creat(glfs_t *fs, const char *path, int flags, mode_t mode);  //3.4.0

int glfs_close(glfs_fd_t *fd);  //3.4.0

ssize_t glfs_read(glfs_fd_t *fd, void *buf, size_t count, int flags);  //3.4.0

ssize_t glfs_write(glfs_fd_t *fd, const void *buf, size_t count, int flags);  //3.4.0

off_t glfs_lseek(glfs_fd_t *fd, off_t offset, int whence);  //3.4.0

int glfs_truncate(glfs_t *fs, const char *path, off_t length);  //3.7.15

int glfs_ftruncate(glfs_fd_t *fd, off_t length, struct glfs_stat *prestat, struct glfs_stat *poststat);  //6.0

int glfs_lstat(glfs_t *fs, const char *path, struct stat *buf);  //3.4.0

int glfs_stat(glfs_t *fs, const char *path, struct stat *buf);  //3.4.0

int glfs_fstat(glfs_fd_t *fd, struct stat *buf);  //3.4.0

int glfs_fsync(glfs_fd_t *fd, struct glfs_stat *prestat, struct glfs_stat *poststat);  //6.0

int glfs_fdatasync(glfs_fd_t *fd, struct glfs_stat *prestat, struct glfs_stat *poststat);  //6.0

int glfs_access(glfs_t *fs, const char *path, int mode);  //3.4.0

int glfs_symlink(glfs_t *fs, const char *oldpath, const char *newpath);  //3.4.0

int glfs_readlink(glfs_t *fs, const char *path, char *buf, size_t bufsiz);  //3.4.0

int glfs_mknod(glfs_t *fs, const char *path, mode_t mode, dev_t dev);  //3.4.0

int glfs_mkdir(glfs_t *fs, const char *path, mode_t mode);  //3.4.0

int glfs_unlink(glfs_t *fs, const char *path);  //3.4.0

int glfs_rmdir(glfs_t *fs, const char *path);  //3.4.0

int glfs_rename(glfs_t *fs, const char *oldpath, const char *newpath);  //3.4.0

int glfs_link(glfs_t *fs, const char *oldpath, const char *newpath);  //3.4.0

glfs_fd_t * glfs_opendir(glfs_t *fs, const char *path);  //3.4.0

int glfs_readdir_r(glfs_fd_t *fd, struct dirent *dirent, struct dirent **result);  //3.4.0

int glfs_readdirplus_r(glfs_fd_t *fd, struct stat *stat, struct dirent *dirent, struct dirent **result);  //3.4.0

int glfs_closedir(glfs_fd_t *fd);  //3.4.0

int glfs_statvfs(glfs_t *fs, const char *path, struct statvfs *buf);  //3.4.0

int glfs_chmod(glfs_t *fs, const char *path, mode_t mode);  //3.4.0

int glfs_fchmod(glfs_fd_t *fd, mode_t mode);  //3.4.0

int glfs_chown(glfs_t *fs, const char *path, uid_t uid, gid_t gid);  //3.4.0

int glfs_fchown(glfs_fd_t *fd, uid_t uid, gid_t gid);  //3.4.0

int glfs_utimens(glfs_t *fs, const char *path, const struct timespec times[2]);  //3.4.0

ssize_t glfs_getxattr(glfs_t *fs, const char *path, const char *name, void *value, size_t size);  //3.4.0

ssize_t glfs_fgetxattr(glfs_fd_t *fd, const char *name, void *value, size_t size);  //3.4.0

ssize_t glfs_listxattr(glfs_t *fs, const char *path, void *value, size_t size);  //3.4.0

ssize_t glfs_flistxattr(glfs_fd_t *fd, void *value, size_t size);  //3.4.0

int glfs_setxattr(glfs_t *fs, const char *path, const char *name, const void *value, size_t size, int flags);  //3.4.0

int glfs_fsetxattr(glfs_fd_t *fd, const char *name, const void *value, size_t size, int flags);  //3.4.0

int glfs_removexattr(glfs_t *fs, const char *path, const char *name);  //3.4.0

int glfs_fremovexattr(glfs_fd_t *fd, const char *name);  //3.4.0

int glfs_fallocate(glfs_fd_t *fd, int keep_size, off_t offset, size_t len);  //3.5.0

int glfs_discard(glfs_fd_t *fd, off_t offset, size_t len);  //3.5.0

int glfs_zerofill(glfs_fd_t *fd, off_t offset, off_t len);  //3.5.0

char * glfs_getcwd(glfs_t *fs, char *buf, size_t size);  //3.4.0

int glfs_chdir(glfs_t *fs, const char *path);  //3.4.0

glfs_fd_t * glfs_dup(glfs_fd_t *fd);  //3.4.0

"""


ffibuilder = FFI()
ffibuilder.set_source(module_name="gfapi_cffi.libgfapi.cffi_libgfapi",
                      source=glfs_c_header_source, libraries=["gfapi"])
ffibuilder.cdef(glfs_cdef)


if __name__ == "__main__":
    project_path = path.abspath(path.join(__file__, "../../../"))
    ffibuilder.compile(tmpdir=project_path, verbose=True)
