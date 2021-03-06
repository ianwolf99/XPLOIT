#define unlink(AV, p,bk,FD)
/*(1) checking if size == the next chunks prev_size*/
*if (chunksize(p) != prev_size(next_chunk(P)))
*malloc_printerr("corrupted size vs prev_size");
FD = P->fd;
BK = p->bk;
/* (2) checking if prev/next chunks correctly points*/
*if (FD->bk != P || BK->fd != P)
* malloc_printerr("corrupted double-link list");
*else {
	FD->bk = BK;
	BK->fd = FD;
} 

//the code is the security checks being perfomed by glibc